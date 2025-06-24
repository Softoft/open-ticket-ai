export const examples = [
    {
        name: 'Drucker',
        subject: 'Drucker reagiert nicht auf Druckbefehle',
        body: `Hallo Support-Team,
mein Büro-Drucker HP OfficeJet Pro druckt seit dem jüngsten Firmware-Update gar nichts mehr. Das Display bleibt dunkel und im System wird der Drucker als “Offline” angezeigt. Ich habe bereits Neustart, zurücksetzen der Netzwerkeinstellungen und den Treiber-Neuinstallationsvorgang versucht – leider ohne Erfolg. Bitte um schnelle Hilfe, da wir dringend Dokumente ausdrucken müssen.`
    },
    {
        name: 'Webinaranmeldung',
        subject: 'Anmeldung zum Webinar „Maschinelles Lernen für Einsteiger“',
        body: `Sehr geehrte Damen und Herren,
ich interessiere mich für Ihr kostenpflichtiges Webinar „Maschinelles Lernen für Einsteiger“ am 25.07.2025. Können Sie mir bitte folgende Informationen zukommen lassen: genaue Veranstaltungszeit, technische Voraussetzungen (z. B. Software, Browser-Version), Preis pro Teilnehmer und Zahlungsmodalitäten? Vielen Dank!`
    },
    {
        name: 'Nest Learning Thermostat',
        subject: 'Nest Thermostat (3. Generation) verliert WLAN-Verbindung',
        body: `Liebes Google-Nest Team,

mein Nest Learning Thermostat der 3. Generation (Seriennummer 04-123-456-789) verbindet sich seit dem letzten Firmware-Update (v5.9.4-2) nicht mehr mit dem Heim-WLAN (Fritz!Box 7590). Es bleibt im Offline-Modus und reagiert nicht auf die App-Befehle. Bitte um kurzfristige Lösung, da die Temperatursteuerung aktuell fehlt.`
    },
    {
        name: 'Netflix-Abo',
        subject: 'Kündigung Netflix Premium Abo (Kundennummer 12345678)',
        body: `Hallo Netflix-Kundenservice,

ich möchte mein Netflix-Premium-Abo zum nächstmöglichen Termin kündigen. Meine Kundennummer lautet 12345678, die hinterlegte E-Mail-Adresse ist max.mustermann@example.com. Bitte senden Sie mir eine Bestätigung der Kündigung und den letzten Abbuchungstermin. Vielen Dank!`
    },
    {
        name: 'WLAN-Ausfall FRITZ!Box',
        subject: 'AVM FRITZ!Box 7590: WLAN fällt alle 10 Minuten aus',
        body: `Sehr geehrtes AVM-Team,

seit gestern fällt das WLAN meiner FRITZ!Box 7590 (Firmware 07.29) im 5-GHz-Band alle 10 Minuten für ca. 30 Sekunden aus. Die 2,4-GHz-Verbindung ist stabil. Ich habe schon Kanal gewechselt und die Box neu gestartet. Bitte um Tipps oder Patch. Danke!`
    },
    {
        name: 'Miele Geschirrspüler',
        subject: 'Miele G 7310 SC: Wasser tritt unten heraus',
        body: `Guten Tag Miele Kundendienst,

bei meinem Miele G 7310 SC (Seriennr. 1234567890) tritt seit heute früh während des Spülvorgangs Wasser aus der unteren Türdichtung aus. Das Gerät ist erst 18 Monate alt und noch in Garantie. Bitte schicken Sie einen Techniker vorbei oder geben Sie eine Reparaturanleitung. Danke!`
    },
    {
        name: 'AWS EC2',
        subject: 'EC2-Instance i-0abcd1234ef567890 nicht per SSH erreichbar',
        body: `Hallo AWS-Support,

meine EC2-Instance mit der ID i-0abcd1234ef567890 im us-east-1 Cluster reagiert seit dem letzten Sicherheits-Update nicht mehr auf SSH-Verbindungen (Port 22). Ich habe die Security Group geprüft, der Key-Pair passt und der Instance-Status ist “running”. Bitte prüfen Sie die Netzwerkkonfiguration oder einen möglichen Hypervisor-Fehler. Vielen Dank!`
    },
    {
        name: 'Booking.com–Reservierung',
        subject: 'Umbuchung Reservierung 1122334455 im Hotel Grand Central',
        body: `Sehr geehrtes Booking.com-Team,

ich möchte meine Reservierung Nr. 1122334455 für das Hotel Grand Central in München vom 15.07.2025 auf den 18.07.2025 verschieben. Die Buchung steht auf den Namen „Müller“. Bitte teilen Sie mir mit, ob der neue Zeitraum verfügbar ist und welche Tarifänderungen anfallen.`
    },
    {
        name: 'SAP Concur API',
        subject: 'Concur-API (v4) gibt 401 Unauthorized zurück',
        body: `Hallo IT-Team,

unsere Anwendung nutzt die SAP Concur REST-API v4 mit Client-ID ABC123 und Secret DEF456. Seit gestern erhalten wir beim Aufruf von /expense/expensereports den HTTP-Status 401 Unauthorized. Token-Refresh schlägt ebenfalls fehl. Bitte prüfen Sie, ob unser Service-Account gesperrt wurde.`
    },
    {
        name: 'Outlook 365 Kalender',
        subject: 'Outlook 365 kalendersync schlägt fehl mit iOS Mail-App',
        body: `Guten Tag Microsoft-Support,

mein Office 365 Business-Account (user@domain.com) synchronisiert den Kalender nicht in der iOS-Mail-App. Ich sehe die Einträge in Outlook Web, aber auf iPhone (iOS 15.6) und iPad (iPadOS 15.6) tauchen sie nicht auf. Ich habe bereits das Konto neu hinzugefügt. Bitte prüfen Sie die OAuth- oder Exchange-Einstellungen.`
    },
    {
        name: 'Garmin Forerunner Update abgebrochen',
        subject: 'Firmware-Update v12.20 bei Garmin Forerunner 945 bricht ab',
        body: `Hallo Garmin-Support,

mein Forerunner 945 (SN G123456789) will seit dem letzten Garmin Connect Update auf v12.20 aktualisieren, bleibt aber bei „Installing… 35%“ stehen und bricht dann ab. Akku voll geladen und Bluetooth-Verbindung stabil. Bitte um Lösungsvorschlag oder manuelles Update-Paket.`
    },
    {
        name: 'Shopify Checkout: Zahlung',
        subject: '“Payment declined” beim Checkout auf my-shop.myshopify.com',
        body: `Liebes Shopify-Team,

mein Kunde versucht, im Shop my-shop.myshopify.com per Kreditkarte (Mastercard) zu zahlen. Die Fehlermeldung lautet “Payment declined: 2004”. In Stripe-Dashboard sehe ich keinen Eintrag. Bitte untersuchen Sie den Zahlungsfluss oder ob es ein Gateway-Problem gibt.`
    },
    {
        name: 'Photoshop',
        subject: 'Adobe Photoshop CC 2022 friert bei großen PSD-Dateien ein',
        body: `Hallo Adobe-Support,

wenn ich in Photoshop CC 2022 (Version 23.4.2) große PSD-Dateien (>1,5 GB) mit mehreren Smart-Objekten öffne, reagiert das Programm nach ~10 Sekunden nicht mehr und wird als “Nicht antwortend” gekennzeichnet. Mein System: Windows 11, 32 GB RAM, RTX 3060. Bitte um Performance-Tipps oder Hotfix.`
    },
    {
        name: 'Tesla Model 3',
        subject: 'Ladeport am Tesla Model 3 (VIN 5YJ3E1EA7LF000316) klemmt',
        body: `Guten Tag Tesla-Service,

bei meinem Model 3 Long Range (VIN 5YJ3E1EA7LF000316) klemmt seit gestern der Ladeport an der Rückseite. Der Ladeanschluss lässt sich nur mit Gewalt öffnen, und die Klappe rastet nicht automatisch ein. Das Auto ist 12 Monate alt. Bitte Termin in der Münchner Werkstatt vereinbaren oder Anweisungen zur temporären Reparatur senden.`
    }
];