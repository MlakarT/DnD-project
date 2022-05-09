<!DOCTYPE html>
<html>
    <head>
        <title>D&D Map Generator</title>
    </head>
    <body>
        <div id="container_left" style="float:left">
            <div class="main_title">
                <svg height="100" width="800">
                    <rect width="530" height="100" style="fill:none;stroke:black;stroke-width:3" />
                    <text x="10" y="66" fill="black" font-size="45" font-family="Lucida Calligraphy">D&D Map Generator</text>
                </svg>
            </div>
            <div id="mapa">
                <div class="inputs" style="float:left">
                    <h2>map</h2>
                    <p>{{seed}}</p>
                    <svg width="600" height="600">
                        <polygon points="0,0 0,120 120,140 240,120 240,0" style="fill:rgb(211,211,211); stroke:rgb(0, 0, 0);stroke-width:3"/>
                        <text x="10" y="70" fill="black" font-size="45" font-family="Lucida Calligraphy">Generate</text>
                    </svg>
                </div>
                <div id="input_boxes">
                </div>
                <div class="map_display" style="float:right">
                    <svg width="400" height="110">
                        <rect width="300" height="100" style="fill:none;stroke-width:3;stroke:rgb(0,0,0)" />
                    </svg>
                </div>
            </div> 
        </div>
    <div id="container_right" style="float:right">
        <div  id="kocke">
            <h2>dice</h2>   
            <ul id="dice_set">
                %for kocka in standardni_set_kock:
                {{standardni_set_kock[kocka]}}
                %end
            </ul> 
        </div>
    </div>  
    </body>
</html>
