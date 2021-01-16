# Generation Z (1997–2012)
# Millennials (1981–1996)
# Generation Xers (1965–1980)
# Baby boomers (1946–1964)
# Silent generation (born between 1928 and 1945)

print('''
Welcome to Generation WHAT!?
              (        (
             ( )      ( )          (
      (       Y        Y          ( )
     ( )     |"|      |"|          Y
      Y      | |      | |         |"|
     |"|     | |.-----| |---.___  | |
     | |  .--| |,~~~~~| |~~~,,,,'-| |
     | |-,,~~'-'___   '-'       ~~| |._
    .| |~       // ___            '-',,'.
   /,'-'     <_// // _  __             ~,\
  / ;     ,-,     \\_> <<_' ____________;_)
  | ;    {(_)} _,      ._>>`'-._          |
  | ;     '-'\_\/>              '-._      |
  |\ ~,,,      _\__            ,,,,,'-.   |
  | '-._ ~~,,,            ,,,~~ __.-'~ |  |
  |     '-.__ ~~~~~~~~~~~~ __.-'       |__|
  |\         `'----------'`           _|
  | '=._                         __.=' |
  :     '=.__               __.='      |
   \         `'==========='`          .'
   '-._                         __.-'
        '-.__               __.-'
             `'-----------'`
''')

generation_alpha = 2013 <= 2025
# "Generation Alpha"
genz_dates = "2013-2025"
generationz = "Generation Z"
genz_dates = "1997–2012"
millennials = "Millennials"
millennials_dates = "1981–1996"
generationx = "Generation Xers"
genx_dates = "1965–1980"
babyboomer = "Baby boomers"
boomer_dates = "1946–1964"
silent_generation = "Silent generation"
silent_dates = "1928-1945"

year_of_birth = input("To get started, enter your year of birth to see what generation you're apart of using the 4 digit year format, e.g. 1960 ")

year_of_birth = int(year_of_birth)

if year_of_birth > 2025:
  print("generation alpha")
elif year_of_birth >= 2013:
    print("generation alpha")
elif year_of_birth >= 2012:
  print("generation z")
elif year_of_birth >= 1997:
    print("generation z")
elif year_of_birth >= 1996:
  print("millennial")
elif year_of_birth >= 1981:
  print("millennial")
elif year_of_birth >= 1980:
  print("generation x")
elif year_of_birth >= 1965:
  print("generation x")
elif year_of_birth >= 1964:
  print("baby boomer")
elif year_of_birth >= 1946:
  print("baby boomer")
elif year_of_birth >= 1945:
  print("silent generation")
elif year_of_birth >= 1928:
  print("silent generation")
else:
  print("sorry, i'm not sure")
