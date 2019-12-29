# 1wire

Raspbian hat die für den 1-Wire-Bus notwendigen Treiber bereits an Bord, wobei der oben erwähnte GPIO 4 für den 1-Wire-Bus vorgesehen ist. Wie bei allen GPIOs werden auch hier die Daten über virtuelle Dateien im Verzeichnis /sys verarbeitet, genauer in:

```
/sys/devices/w1_bus_master/
```

Die One-Wire-Schnittstelle muß in der Datei /boot/config.txt aktiviert, indem dort zwei Zeilen eingetragen werden:

```
dtoverlay=w1-gpio,gpiopin=4 
```

Damit wird der Pin 4 des GPIO für One Wire reserviert. Oder, falls noch der interne Pullup-Widerstand geschaltet werden soll:

```
dtoverlay=w1-gpio-pullup,gpiopin=4,extpullup=on
```
