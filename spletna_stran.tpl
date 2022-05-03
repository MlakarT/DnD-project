<!DOCTYPE html>
<html>
    <head>
        <title>D&D map generator</title>
    </head>
    <body>
        <h1 id="main_title">D&D MAP GENERATOR</h1>
        <div id="mapa">
            <h2>map</h2>
            <p>{{seed}}</p>
            <svg width="400" height="110">
                <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
              </svg>
        </div>
        <div  id="kocke">
            <h2>dice</h2>   
            <ul id="dice_set">
                %for kocka in standardni_set_kock:
                {{standardni_set_kock[kocka]}}
                %end
            </ul> 
        </div>
    </body>
</html>
