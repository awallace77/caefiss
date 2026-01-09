-- CAF-159: Reporter information - updated values
-- Updated values for reporter information

WHENEVER SQLERROR EXIT FAILURE ROLLBACK;
SET ECHO ON
SPOOL 3_CAF-159.log
ALTER SESSION SET CURRENT_SCHEMA=CAEFISS_OWNER;

UPDATE CAEFISS_OWNER.CD_SETTING
SET ENGLISH_VALUE='Public Health Unit',
	FRENCH_VALUE='Unité de santé publique'
WHERE id=2;

UPDATE CAEFISS_OWNER.CD_REPORTER_PROF_STATUS
SET ENGLISH_VALUE='Active Pediatric Surveillance',
	FRENCH_VALUE='Surveillance pédiatrique active'
WHERE id=3;

commit;

SPOOL OFF
