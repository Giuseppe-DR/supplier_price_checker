import tabula

# convert PDF into CSV
tabula.convert_into("C:\\Users\\Giuseppe\\Desktop\\TryNullParam.pdf", "output.csv", output_format="csv", pages='all')
