#
#
#
# Project Names.
###############################################################################

PROJECT_NAME:=$(notdir $(CURDIR))
EXEC_NAME:=a.out
TARGET_EXEC:=$(bindir)/$(EXEC_NAME)


# General / Misc Variables.
###############################################################################
DATE:=$(shell date +%d/%m/%Y-%T)
TAR_NAME:=$(LOGNAME)-$(PROJECT_NAME)-$(DATE)
ZIP_NAME:=$(TAR_NAME)

ARCHIVE_DIR:=../../.ARCHIVES
ARCHIVE_GROUP_NAME:=$(LOGNAME)-$(PROJECT_NAME)-ARCHIVE-V0
ARCHIVE_GROUP:=$(ARCHIVE_DIR)/$(ARCHIVE_GROUP_NAME)
ARCHIVE_NAME:=$(ARCHIVE_GROUP)/$(PROJECT_NAME)-ARCHIVE


# Makefile Rules.
###############################################################################
.PHONY: save archive 


###############################################################################
# "save" "archive"
#  Rules for Saving / Archiving (making a copy of the contents of this Project).
#
save archive: $(ARCHIVE_NAME)
	@cp -a . $(ARCHIVE_NAME)/.

$(ARCHIVE_NAME): $(ARCHIVE_GROUP)
	@mkdir -p $@
$(ARCHIVE_GROUP): $(ARCHIVE_DIR)
	@mkdir -p $@
$(ARCHIVE_DIR):
	@mkdir -p $@



