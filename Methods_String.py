# Return a copy of the string with all the cased characters converted to lowercas"
s="ARYAN"
print(s.lower())  # Output: aryan

# Return a copy of the string with all the cased characters converted to lowercase.
s="Aryan"
print(s.lower())
# output: aryan
# Return a copy of the string with all the cased characters converted to uppercase.
s1="aryan singh"
print(s1.upper())

# Return a title cased version of the string where words start with an uppercase character and the remaining characters are lowercase.
s2="Methods of String"
print(s2.title())
# output : Methods of String

# The capitalize() Return a copy of the string with its first character capitalized and the rest lowercased.
s3="hello world"
print(s3.capitalize())
# output : Hello world

# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
s4="Hello World"
print(s4.swapcase())
# output : hELLO wORLD

# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss"

s5="ß"
print(s5.casefold())
# output : ss

# Return a copy of the string with the leading and trailing characters removed.
s6="   Hello World  This Is First Python Program      "
print(s6.strip())
# output : Hello World  This Is First Python Program

# Return a copy of the string with leading characters removed. 
s7="   Hello  "
print(s7.lstrip())
# output : Hello

# Return a copy of the string with trailing characters removed. 
s8="   Hello  "
print(s8.rstrip())
# output :    Hello

