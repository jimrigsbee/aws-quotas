#!/bin/bash
for region in rht-vt ext-vt rht-na rhu-na rht-eu rhu-eu rht-la rhu-la rht-ap rhu-ap rht-anz rhu-anz prod dev; do
  python main.py --profile ${region}
done
