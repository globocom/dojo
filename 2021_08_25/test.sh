#!/bin/sh
make test
ret=$?

set -e
sed -i '/workbench.colorCustomizations/, +99 d' .vscode/settings.json

if [ $ret -eq 0 ]; then
    cat >> .vscode/settings.json <<EOF
  "workbench.colorCustomizations": {
    "statusBar.background": "#029400",
    "statusBar.noFolderBackground": "#029400",
    "statusBar.debuggingBackground": "#029400",
    "activityBar.background": "#014400"
  }
}
EOF

else
    cat >> .vscode/settings.json <<EOF
  "workbench.colorCustomizations": {
    "statusBar.background": "#940000",
    "statusBar.noFolderBackground": "#940000",
    "statusBar.debuggingBackground": "#940000",
    "activityBar.background": "#5d0000"
  }
}
EOF

fi