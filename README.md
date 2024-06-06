# SP-GENERATOR

Spotify Account Generator (KALI LINUX!)

## Përshkrimi

SP-GENERATOR është një mjet për të krijuar llogari të reja në Spotify në mënyrë automatike. Ky mjet është krijuar për t'u përdorur në sistemet operative Kali Linux dhe përdor kërkesa HTTP për të krijuar llogaritë.

## Karakteristikat

- Gjeneron emra përdoruesish dhe fjalëkalime të rastësishme.
- Mund të krijojë disa llogari njëkohësisht.
- Opsion për të ruajtur llogaritë e krijuara në një skedar të jashtëm.

## Kërkesat

- Python 3.x
- Paketa `requests`

## Instalimi

1. Sigurohu që ke instaluar Python 3 dhe menaxherin e paketave `pip`.
2. Instalo varësitë e nevojshme:

    ```sh
    pip install requests
    ```

3. Klono depotinë nga GitHub dhe navigo në direktoriumin e projektit:

    ```sh
    git clone https://github.com/Mirsadnee/Generator
    cd Generator
    ```

4. Ekzekuto skriptin:

    ```sh
    python3 SP-GENERATOR.py
    ```

## Përdorimi

1. Për të gjeneruar një llogari dhe për ta printuar atë në terminal:

    ```sh
    python3 SP-GENERATOR.py
    ```

2. Për të gjeneruar disa llogari, përdor opsionin `-n` për të specifikuar numrin e llogarive:

    ```sh
    python3 SP-GENERATOR.py -n 5
    ```

3. Për të ruajtur llogaritë e gjeneruara në një skedar, përdor opsionin `-o` për të specifikuar emrin e skedarit:

    ```sh
    python3 SP-GENERATOR.py -n 3 -o llogarit.txt
    ```

## Shembuj

- Për të gjeneruar 5 llogari dhe për t'i printuar ato në terminal:

    ```sh
    python3 SP-GENERATOR.py -n 5
    ```

- Për të gjeneruar 3 llogari dhe për t'i ruajtur ato në një skedar të quajtur `llogarit.txt`:

    ```sh
    python3 SP-GENERATOR.py -n 3 -o llogarit.txt
    ```

## Autori

- Emri: Volpino
- GitHub: [volpinottv](https://github.com/volpinottv)

## Licensa

Ky projekt është nën licensën MIT. Për më shumë informacion, shiko skedarin [LICENSE](LICENSE).

## Shënime

Ky mjet është për qëllime edukative dhe testimi. Përdorimi i tij për qëllime keqdashëse ose të paligjshme është i ndaluar dhe i dënueshëm me ligj.
