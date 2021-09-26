import np
import pandas as pd
import geopandas as gp
import folium
from osgeo import gdal

from image.core import Image


class GeoTiff(Image, gp.GeoDataFrame):
    def __init__(self, ds, name):
        self.ds = ds
        img = ds.GetRasterBand(1).ReadAsArray()
        self.cols = ds.RasterXSize
        self.rows = ds.RasterYSize
        self.shape = np[self.rows, self.cols]
        self.geotransform = np.array(ds.GetGeoTransform())
        self.xmin = geotransform[0]
        self.xmax = np[1, cols] @ geotransform[:2]
        self.xbounds = np[self.xmin, self.xmax]
        self.ymin = np[1, rows] @ geotransform[3:6:2]
        self.ymax = geotransform[3]
        self.ybounds = np[self.ymin, self.ymax]
        self.centerx = self.xbounds.mean()
        self.centery = self.ybounds.mean()
        self.center = np[self.centerx, self.centery]

        path = ds.getDescription()

        self.df = pd.DataFrame(img, index=np.linspace(self.ymin, self.ymax, self.rows), columns=np.linspace(self.xmin, self.xmax, self.cols)).stack(
        ).replace(0, np.nan).dropna().reset_index().rename(columns={"level_1": "Longitude", "level_0": "Latitude", 0: "Intensity"})

        gp.GeoDataFrame.__init__(self.df, geometry=gp.points_from_xy(
            self.df.Longitude, self.df.Latitude))
        Image.__init__(self, img=img, name=name, path=path)

    @classmethod
    def open(cls, path: str, name: str = ""):
        return cls(gdal.Open(path, gdal.GA_ReadOnly), name=name)

    @classmethod
    def read(cls, path: str, name: str = ""):
        return cls(gdal.Open(path, gdal.GA_ReadOnly), name=name)

    def folium(self):
        m = folium.Map(location=self.center, zoom_start=1,
                       tiles='Stamen Terrain')
        folium.raster_layers.ImageOverlay(
            image=ds.GetRasterBand(1).ReadAsArray(),
            bounds=[[ymin, xmin], [ymax, xmax]],
            colormap=lambda x: (1, 0, x, x),  # R,G,B,alpha
        ).add_to(m)

        incidents = folium.map.FeatureGroup()
        pd.DataFrame.apply(self, lambda row: incidents.add_child(folium.CircleMarker([row.Latitude, row.Longitude], radius=5, color='yellow', fill=True, fill_color='blue', fill_opacity=0.6)) and folium.Marker(
            [row.Latitude, row.Longitude], popup=f"<span style=\"color:#0000FF\">{row.Intensity}</span>").add_to(m), axis=1)
        m.add_child(incidents)
        return m
