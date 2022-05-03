<!DOCTYPE html>
<html>
    <head>
        <title>D&D map generator</title>
    </head>
    <body>
        <h1 id="main_title">D&D MAP GENERATOR</h1>
        <div id="mapa">
            <h2>map</h2>
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
