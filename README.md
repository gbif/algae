# GBIF Algae Classification
A classification for [all algae from kingdom down to families](algae.txt) distributed across the 3 kingdoms Plantae, Chromista and Protozoa.
The project is setup so that the github zip represents a valid Darwin Core Checklist Archive, synonyms are included.

This classification is aiming to fill the algae gaps in the current Catalog of Life which has no taxa within the following phyla:
 - Chromista: Cryptophyta, Haptophyta, Ochrophyta
 - Plantae: Charophyta, Chlorophyta, Glaucophyta, Rhodophyta
 - Protozoa: Euglenozoa

The classification is registered in GBIF as http://www.gbif.org/dataset/7ea21580-4f06-469d-995b-3f713fdcc37c

## Classification details
The [derived algae classification](algae.txt) includes all missing CoL phyla (see below) and also the missing protozoa phyla *Loukozoa* and *Metamonada*

# Source classifications reviewed
The following classifications have been used as sources to create the algae classification.

### CoL - current
```
Chromista
  Bigyra
  Ciliophora
 *Cryptista
  Foraminifera
 *Haptophyta
  Miozoa
 *Ochrophyta
  Oomycota
  Radiozoa
Plantae
  Anthocerotophyta
  Bryophyta
 *Charophyta
 *Chlorophyta
 *Glaucophyta
  Marchantiophyta
 *Rhodophyta
  Tracheophyta
Protozoa
  Amoebozoa
  Cercozoa
  Choanozoa
 *Euglenozoa
 *Loukozoa
 *Metamonada
  Microsporidia
  Mycetozoa
  Percolozoa
  Sarcomastigophora
 *Sulcozoa
  
* = empty taxon with no children. Mostly missing due to removal of Algaebase
```

As we use the entire CoL classification we primarily aim at filling in the gaps of these empty phyla:
For Protozoa we will only treat the "algae" phylum Euglenozoa:

 - Chromista
    - Cryptista aka Cryptophyta
    - Haptophyta
    - Ochrophyta
 - Plantae
    - Charophyta
    - Chlorophyta
    - Glaucophyta
    - Rhodophyta
 - Protozoa
    - Euglenozoa

### GBIF Backbone 2013
Classification down to families for the entire kingdoms [Plantae, Chromista and Protozoa](backbone2013/nub-full.txt)
A filtered version with just the seeked [algae phyla](backbone2013/nub-algae.txt)

### ITIS
Classification down to families: [plantae](itis/itis-plantae.md), [chromista](itis/itis-chromista.md) & [protozoa](itis/itis-protozoa.md)

### WoRMS
Classification down to families for the kingdoms: [plantae](worms/worms-3.txt), [chromista](worms/worms-7.txt) & [protozoa](worms/worms-5.txt)

### Algaebase
Hard to access and the bad guy who requested removal from CoL and prevends WoRMS from sharing

### Ruggiero 2015
See [PLOS article 10.1371/journal.pone.0119248](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0119248)
Also available as strangely formatted [Excel spreadsheet](journal.pone.0119248.s002.XLSX).

### Smithsonian
http://botany.si.edu/projects/algae/classification.htm

 1. BACILLARIOPHYTA (diatoms)
 1. CHAROPHYTA (stoneworts)
 1. CHLOROPHYTA (green algae)
 1. CHRYSOPHYTA (golden algae)
 1. CYANOBACTERIA (blue-green algae)
 1. DINOPHYTA (dinoflagellates)
 1. PHAEOPHYTA (brown algae)
 1. RHODOPHYTA (red algae)

