from django.shortcuts import render
import numpy as np
import matplotlib
from matplotlib import colors
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os
import earthpy.plot as ep
import earthpy.spatial as es
from pysolar.solar import *
import datetime
import pytz
import ipywidgets as widgets
import elevation
from io import StringIO

# Create your views here.
def home_page(request):

    if request.method == "POST":
        chosen_date=request.POST.get('datetimepicker')
        chosen_date=datetime.datetime.strptime(chosen_date, "%Y/%m/%d %H:%M")
        timezone=pytz.timezone('MST')
        chosen_date=timezone.localize(chosen_date)
    else:
        chosen_date=datetime.datetime.now()
        timezone = pytz.timezone('MST')
        chosen_date=chosen_date.astimezone(tz=timezone)

    #teton_dem = rd.LoadGDAL('Teton-30m-DEM.tif')
    #aspect = rd.TerrainAttribute(teton_dem, attrib='aspect');
    #slope = rd.TerrainAttribute(teton_dem, attrib='slope_riserun');

    #np.save('aspect.npy', aspect)
    #np.save('elevation.npy', teton_dem)
    #np.save('slope.npy',slope)

    #aspect_array=np.load('aspect.npy')
    #elevation_array=np.load('elevation.npy')
    #slope_array=np.load('slope.npy')

    #danger_graph(elevation_array)
    azimuth=get_azimuth(43.75, -110.8, chosen_date)

    context={}
    context['chosen_date']=chosen_date
    context['azimuth']=azimuth

    return render(request,'home_page.html',context)

def danger_graph(elevation_array):
    cmap = ListedColormap(["green", "yellow", "orange","red","black"])
    norm = colors.BoundaryNorm([0, 1828.8, 2286, 2743.2, 3200.4], 5)

    fig, ax = plt.subplots()
    ep.plot_bands(elevation_array,cmap=cmap,cbar=False,title="Teton Area Danger Rating",norm=norm,ax=ax)
    hillshade=es.hillshade(elevation_array)
    ax.imshow(hillshade, cmap="Greys", alpha=0.5)

    fig.savefig('danger_graph.png')


