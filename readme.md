# side-matrix
> Control the text of a LED matrix with serial commands

## Command format
`[id][key][whaever]\n` The script will look for the device ID on the first character of the string, then it will get the key to find the texts on `texts.json`