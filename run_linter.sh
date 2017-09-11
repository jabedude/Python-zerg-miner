#!/usr/bin/env bash
IFS=' '
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

FAILURE=0

PEP8=$(pep8 .)

if [ "$PEP8" ]; then
    echo -e "\n${RED}- pep8 violations:${NC}"
    echo -e "${RED}$PEP8${NC}"
    echo ""
    FAILURE=1
else
    echo -e "${GREEN}+ pep8${NC}"
fi

exit $FAILURE
