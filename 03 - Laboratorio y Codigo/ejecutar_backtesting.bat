@echo off
setlocal
cd /d "%~dp0"
title Master de Riesgos - Backtesting Cuantitativo VaR
color 0B

echo ==============================================================
echo     INICIANDO AUDITORIA CUANTITATIVA - MASTER DE RIESGOS
echo ==============================================================
echo.

python "backtesting_var.py"

if errorlevel 1 (
    echo.
    echo [ERROR] Hubo un problema al ejecutar el script de Python.
    pause
)
endlocal
