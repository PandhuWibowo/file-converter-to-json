import tabula

# Read pdf into DataFrame
# df = tabula.read_pdf("test.pdf", pages='all')

# Read remote pdf into DataFrame
tabula.convert_into("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf", "liat.csv", output_format="csv")

# convert PDF into CSV
# tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

# # convert all PDFs in a directory
# tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')