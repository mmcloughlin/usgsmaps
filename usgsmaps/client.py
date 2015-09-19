import pyproj
import requests


def _bbox(lat, lng, delta=0.001):
    """
    Return bounding box around the given (lat,lng), in EPSG:3857. This is
    prurely intended for constructing the bbox parameter in requests.
    """
    wgs84 = pyproj.Proj(init='EPSG:4326')
    epsg3857 = pyproj.Proj(init='EPSG:3857')
    sw = pyproj.transform(wgs84, epsg3857, lng - delta, lat - delta)
    ne = pyproj.transform(wgs84, epsg3857, lng + delta, lat + delta)
    return '%f,%f,%f,%f' % (sw[0], sw[1], ne[0], ne[1])


def raw(lat, lng, num=50):
    """
    Query USGS for maps of the given (lat,lng). Returns raw GeoJSON response.
    """
    url = 'http://usgsvm1.srv.mst.edu/geoserver/mlad/wms'
    params = {}
    params['version'] = '1.1.1';
    params['service'] = 'wms';
    params['request'] = 'getFeatureInfo';
    params['srs'] = 'EPSG:3857';
    params['height'] = 480;
    params['width'] = 640;
    params['bbox'] = _bbox(lat, lng);
    params['x'] = 170; # XXX
    params['y'] = 208; # XXX
    params['exceptions'] = 'application/vnd.ogc.se_xml';
    params['feature_count'] = num;
    params['format'] = 'image/png';
    params['styles'] = '';
    params['layers'] = 'mlad_products';
    params['query_layers'] = 'mlad_products';
    params['info_format'] = 'application/json';
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()
