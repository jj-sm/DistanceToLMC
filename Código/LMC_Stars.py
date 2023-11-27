from astroquery.gaia import Gaia
import numpy as np

# Centro de la región
ra_lmc = 80.893
dec_lmc = -69.756

# Estrellas a la redonda
query = f'''
SELECT TOP 1000000
       source_id, ra, dec, parallax, pmra, pmdec, phot_g_mean_mag
FROM gaiadr2.gaia_source
WHERE 1=CONTAINS(POINT('ICRS', gaiadr2.gaia_source.ra, gaiadr2.gaia_source.dec),
                 CIRCLE('ICRS', {ra_lmc}, {dec_lmc}, 15.0))
'''
job = Gaia.launch_job(query)
result = job.get_results()

# CSV
result.write('Estrellas_GAIA5.csv', overwrite=True)

