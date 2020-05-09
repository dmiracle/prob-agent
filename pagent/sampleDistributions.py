distributions = {
    'sex': [1, ['M', 'F']],
    'normal': ["normal", 0, 0.2],
    'age' : ["interpolate", [(0, 1), (100, 0)]],
}
dndstats = {
        'str' : ["dice", (3, 6)],
        'dex' : ["dice", (3, 6)],
        'con' : ["dice", (3, 6)],
        'int' : ["dice", (3, 6)],
        'wis' : ["dice", (3, 6)],
        'cha' : ["dice", (3, 6)] 
}
iui = {
    'pregnant': [[.15, .85], [True, False]]
}