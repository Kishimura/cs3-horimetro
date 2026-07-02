[Setup]
AppName=Calculadora de Horimetro
AppVersion=1.0.0
DefaultDirName={autopf}\Calculadora de Horimetro
DefaultGroupName=Calculadora de Horimetro
OutputDir=output
OutputBaseFilename=Instalador_Calculadora_Horimetro
Compression=lzma
SolidCompression=yes
SetupIconFile=..\assets\icone.ico
UninstallDisplayIcon={app}\Calculadora_Horimetro.exe

[Files]
Source: "..\dist\Calculadora_Horimetro\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Calculadora de Horimetro"; Filename: "{app}\Calculadora_Horimetro.exe"; IconFilename: "{app}\Calculadora_Horimetro.exe"
Name: "{commondesktop}\Calculadora de Horimetro"; Filename: "{app}\Calculadora_Horimetro.exe"; IconFilename: "{app}\Calculadora_Horimetro.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na area de trabalho"; GroupDescription: "Atalhos:"