import codecs
sourceFileName="tweets2.json"
targetFileName="tweets2c.json"

BLOCKSIZE = 1048576 # or some other, desired size in bytes
with codecs.open(sourceFileName, "r", "utf-8") as sourceFile:
    with codecs.open(targetFileName, "w", "utf-16") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)
            print contents.encode("utf-8")