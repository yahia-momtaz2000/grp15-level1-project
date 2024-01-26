# program to swap comma by dot, dot by comma

statement = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football.'
print(statement)
statement = statement.replace(',','*')
statement = statement.replace('.', ',')
statement = statement.replace('*', '.')
print(statement)


