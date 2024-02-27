import random
from dia_3 import tinder
from dia_2 import seguidor_aleatorio
fichero = "ships.js"
seguidores = ["mxuspldu", "adua_viles", "elcolumpiooficial",
              "joel_serebin", "_maxiivc", "michaell_morraz",
               "popmillpye", "lorrain_1", "moha.gmt_15",
                "david.siqueiros.56884", "filip_samuel14",
                 "herr_oktopus", "davidponce1522", "buty0606",
                  "jonnierdev", "ferrodriguxz", "spillwayallay",
                   "cesarsanchez", "er.en_data", "danielmendoza847",
                     "andres.jimenez.3705157", "eduarholguin", 
                     "sr.kitsune_", "nickoloko456", "joshu_alop"]
print(seguidor_aleatorio(1, seguidores))
tinder(seguidores, fichero)