#!/bin/bash
# @author: Paul DiCarlo
# @copyright: 2025 Paul DiCarlo
# @license: MIT
# @contact: https://github.com/pauldicarlo


export PEAK_X=213
export PEAK_Y=510
export THROAT_X=10
export THROAT_Y=233
export TACK_X=0
export TACK_Y=0
export CLEW_X=397 
export CLEW_Y=29 


cat > request.json << EOF
{
  "peak_x": $PEAK_X,
  "peak_y": $PEAK_Y,
  "clew_x": $CLEW_X,
  "clew_y": $CLEW_Y,
  "tack_x": $TACK_X,
  "tack_y": $TACK_Y,
  "throat_x": $THROAT_X,
  "throat_y": $THROAT_Y
}
EOF


export API_PATH=sailocus/api/v1/coe/ 


# Execute curl using the substituted JSON file
curl -v -X POST "https://localhost:8000/${API_PATH}" \
  -H "Content-Type: application/json" \
  -d @request.json \
  --cert certs/client.crt \
  --key certs/client.key \
  --cacert certs/ca.crt \
  --output coordinate_point.svg
