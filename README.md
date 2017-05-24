## lookup_uk

General information about this repo.

Folders:
originals folder contains the files as they were downloaded.
write folder countains script to self written/combined lookup files.

Below are small descriptions  of the files which have been slightly modified.
Ex of Modifications:
- Renaming the files to make content more obvious.
- Renaming columns to make content more obvious.
- Make columns names consistent across files to make it easier to write functions for automatic lookup eventually.
- Combining different lookups together.

If you’re not use to output areas, don’t get confuse by the names, lower super output areas (LSOA) are larger than output areas (they are generally made up of four to six output areas), it’s the “super” that matters here not the “lower”. This is done to allow data provider to release content that could be disclosive if published by output areas.


Yes I will need to put this in a clean little json eventually. That’s far from being a priority for me however, so if you want to take the lead and do it, thanks. :)

—————————————————————————————————————

#### oa_to_pcs.csv 
Matches output areas to postcode sector for England and Wales. The original for this was published by the ONS in August 2016. The output areas are those of 2011. Relations are not unique, more than one lower super output area can be match to the same postcode.
*Not sure why there are some double space in some postcodes. Might be so they fit eight character postcode format, rather than seven charactre format.*

—————————————————————————————————————

#### pc_to_oa_lsoa_msoa_lad.csv
Matches postcodes (seven and eight character format) to output areas, lower super output areas (code and name), middle super output areas (code and name), local authority district (code, name and welsh name) for England and Wales. The original for this was published in August 2016. The outuput areas are those of 2011. There is a boolean numeric indicator to know if the postcode is split between more than one output area (“1” if True, “0” if False). They are however linked to only one output area in the file, “best-fitted by plotting to the postcode’s mean”.

—————————————————————————————————————

#### lad_to_county.csv
Matches lad (code and name) to county (code and name) for England (be aware this exludes unitary authorities). The original for this was published in January 2017.

—————————————————————————————————————

#### pc_to_oa_lsoa_msoa_lad_county.csv
Matches postcodes (seven and eight character format) to output areas, lower super output areas (code and name), middle super output areas (code and name), local authority district (code, name and welsh name) and county (be aware this excludes unitary authority) for England and Wales. This is the combination of pc_to_oa_lsoa_msoa_lad.csv and lad_to_county.csv using add_county_to_lad.py in the write folder.

—————————————————————————————————————
