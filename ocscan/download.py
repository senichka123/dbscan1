from astroquery.gaia import Gaia
import pandas as pd
import os


def gaiadata(ra, dec, radius = 0.0833, SaveData = False):
    
    """Download data from Gaia DR 2 in circle with set coordinates
    
    Arguments
    ----------
    ra : float
    Right Accesion (in degrees)
    
    dec : float
    Declination (in degrees)
    
    radius : float
    Sky field radius (in degrees)
    radius_default = 0.0833 deg -> 5 arcmin
    
    Returns
    -------
    file : data.csv
    
    """
    
    query = "SELECT ra, dec, ra_error, dec_error, parallax, parallax_error, pmra, pmra_error, pmdec, pmdec_error, phot_g_mean_mag, bp_rp, r_est, r_lo, r_hi FROM external.gaiadr2_geometric_distance JOIN gaiadr2.gaia_source USING (source_id) WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',"+str(ra)+","+str(dec)+","+str(radius)+"))=1"
    job = Gaia.launch_job(query, output_file='data.csv',output_format='csv',dump_to_file=SaveData)
    results = job.get_results()
    data = results.to_pandas()
    #data=pd.read_csv('data.csv')
    data.rename(columns={'ra': 'RA_ICRS', 'dec': 'DE_ICRS', 'parallax': 'Plx', 'pmra': 'pmRA', 'pmdec': 'pmDE', 'phot_g_mean_mag': 'Gmag','bp_rp': 'BP_RP'},inplace=True)
	
    return data
#gaiadata.__doc__ = """Download data from Gaia DR 2 in circle with set coordinates"""
#Examples
#--------
#>>> from download import gaiadata
#>>> gaiadata(50, 50)