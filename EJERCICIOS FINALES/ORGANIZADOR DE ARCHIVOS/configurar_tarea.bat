@echo off
echo Configurando tarea automática para el organizador de archivos...

REM Crear tarea que se ejecute cada 30 minutos
schtasks /create /tn "OrganizadorArchivos" /tr "C:\Users\nicol\OneDrive\Escritorio\FORMACION ACADEMICA\SANTANDER PYTHON CON CURSOR\EJERCICIOS FINALES\ORGANIZADOR DE ARCHIVOS\auto_organizador.bat" /sc minute /mo 30 /f

echo Tarea creada exitosamente!
echo La tarea se ejecutará cada 30 minutos.
echo Para ver las tareas: schtasks /query /tn "OrganizadorArchivos"
echo Para eliminar la tarea: schtasks /delete /tn "OrganizadorArchivos" /f
pause
