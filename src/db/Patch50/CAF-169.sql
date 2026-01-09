-- CAF-169: AEFI impact, outcome, care obtained -updated values
-- Updated values for AEFI IOC

WHENEVER SQLERROR EXIT FAILURE ROLLBACK;
SET ECHO ON
SPOOL 4_CAF-169.log
ALTER SESSION SET CURRENT_SCHEMA=CAEFISS_OWNER;

UPDATE CAEFISS_OWNER.CD_OUTCOME
SET ENGLISH_VALUE='Persistent or significant disability/incapacity',
	FRENCH_VALUE='Invalidité/incapacité persistante ou importante'
WHERE id=2;

UPDATE CAEFISS_OWNER.CD_HIGHEST_CARE
SET ENGLISH_VALUE='Telephone/virtual consultation with Health Care Provider',
	FRENCH_VALUE='Consultation téléphonique/virtuelle avec un professionnel de la santé'
WHERE id=2;

commit;

SPOOL OFF
