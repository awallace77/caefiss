
-- CAF-491: Updated French Translations

WHENEVER SQLERROR EXIT FAILURE ROLLBACK;
SET ECHO ON
SPOOL 13_CAF-491.log
ALTER SESSION SET CURRENT_SCHEMA=CAEFISS_OWNER;
   
UPDATE CD_AEFI_FIELDS
    SET FRENCH_VALUE = 'Champ du problème de suivi' 
    WHERE ID = 265;

commit;

UPDATE CD_AEFI_FIELDS
    SET ENGLISH_VALUE = 'Recent immunization history: Please indicate below any other vaccine(s) received within 30 days prior to the "date vaccine administered" reported in the Vaccine tab' 
    WHERE ID = 58;
commit;

UPDATE CD_AEFI_FIELDS
    SET FRENCH_VALUE = 'Historique récent de vaccination : Veuillez indiquer ci-dessous tout autre vaccin reçu dans les 30 jours précédant la « date d’administration du vaccin » indiquée dans l’onglet Vaccin.' 
    WHERE ID = 58;
    
commit;

SPOOL OFF
