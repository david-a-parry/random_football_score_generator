#!/bin/bash
# hacky way of downloading score data - could be improved so that it
# automatically determines available seasons

set -euo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
echo $(date) removing old data
rm -r [1-2]*

echo $(date) downloading new data
perl $DIR/download.pl | bash - 

echo $(date) finished
