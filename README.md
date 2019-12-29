# 1wire

Raspbian hat die für den 1-Wire-Bus notwendigen Treiber bereits an Bord, wobei der oben erwähnte GPIO 4 für den 1-Wire-Bus vorgesehen ist. Wie bei allen GPIOs werden auch hier die Daten über virtuelle Dateien im Verzeichnis /sys verarbeitet, genauer in:

```
/sys/devices/w1_bus_master/
```

Die One-Wire-Schnittstelle muß über ```raspi-config``` --> ```5 Interface Options``` aktiviert werden.
