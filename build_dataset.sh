mkdir data
wget https://opac.rism.info/fileadmin/user_upload/lod/update/rismAllMARCXML.zip -O ./data/rism_data.zip && unzip ./data/rism_data.zip
find ./data/ ! -name 'rism_231219.xml' -type f -exec rm -f {} +

python extractor.py
python converter.py