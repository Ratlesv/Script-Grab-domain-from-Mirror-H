import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))