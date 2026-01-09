
-- CAF-172: Case Management - Case update table - all changes
-- New fields and updated values for the Case Management - Case Update table
WHENEVER SQLERROR EXIT FAILURE ROLLBACK;
SET ECHO ON
SPOOL 13_CAF-172-patch.log
ALTER SESSION SET CURRENT_SCHEMA=CAEFISS_OWNER;

-- CORRECTION - Set status to 0 instead of DELETE
UPDATE CD_CASE_UPDATE 
	SET STATUS = 0
	WHERE ID = 1;

UPDATE CD_CASE_UPDATE_AUD
	SET STATUS = 0
 	WHERE ID = 1;
commit;

SPOOL OFF;
