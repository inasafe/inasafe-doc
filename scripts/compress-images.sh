#!/bin/bash
for FILE in `find ./docs/resources -type f -size +200k -name "*.png" ! -path "./safe_qgis/test/test_data/test_images/*"`
do 
    echo "Compressing $FILE"
    mogrify -dither FloydSteinberg -colors 256 -antialias -strip $FILE
done
