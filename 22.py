a = str(input())
b = str(input())
if ( sorted(a) == sorted(b) ):
    print( "They are anagrams" )
else:
    print( "They are not anagrams" )