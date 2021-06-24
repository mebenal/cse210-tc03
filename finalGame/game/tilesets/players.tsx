<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.5" tiledversion="1.7.0" name="01-generic" tilewidth="16" tileheight="16" tilecount="120" columns="15">
 <image source="../images/01-generic.png" width="240" height="128"/>
 <tile id="0">
  <animation>
   <frame tileid="0" duration="250"/>
   <frame tileid="1" duration="250"/>
   <frame tileid="2" duration="250"/>
   <frame tileid="1" duration="250"/>
  </animation>
 </tile>
 <tile id="1">
  <objectgroup draworder="index" id="2">
   <object id="1" x="2" y="16">
    <polygon points="0,0 0,-16 13,-16 13,0"/>
   </object>
  </objectgroup>
 </tile>
</tileset>
