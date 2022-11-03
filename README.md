# dyn-ec2-allpurposes-tagging

zip dyn-ec2-allpurposes-tagging.zip dyn-ec2-allpurposes-tagging.py
```
aws lambda create-function --function-name dyn-ec2-allpurposes-tagging \
  --runtime python3.9 --role arn:aws:iam::<account-id>:role/AWSLambda-TaggingAutomations \
  --handler dyn-ec2-allpurposes-tagging.lambda_handler --timeout 10 --zip-file fileb://./dyn-ec2-allpurposes-tagging.zip \
  --region eu-west-2 --profile default
```   
aws lambda update-function-configuration --function-name dyn-ec2-allpurposes-tagging \
  --zip-file fileb://./dyn-ec2-allpurposes-tagging.zip --region eu-west-2 --profile default
   
aws events put-rule --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EBS Multi-Volume Snapshots Completion Status\"],\"detail\":{\"event\":[\"createSnapshots\"],\"result\":[\"succeeded\"]}}" \
  --state ENABLED --name dyn_snp_multi_volume_lambda_tagging_rule --region eu-west-2 --profile default
   
aws events put-rule --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EBS Multi-Volume Snapshots Completion Status\"],\"detail\":{\"event\":[\"createSnapshots\"],\"result\":[\"succeeded\"]}}" \
  --state ENABLED --name dyn_snp_multi_volume_lambda_tagging_rule --region eu-west-1 --profile default

aws events put-rule --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EBS Snapshot Notification\"],\"detail\":{\"event\":[\"createSnapshot\"],\"result\":[\"succeeded\"]}}" \
  --state ENABLED --name dyn_snp_lambda_tagging_rule --region eu-west-2 --profile default
   
aws events put-rule --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EBS Snapshot Notification\"],\"detail\":{\"event\":[\"createSnapshot\"],\"result\":[\"succeeded\"]}}" \
  --state ENABLED --name dyn_snp_lambda_tagging_rule --region eu-west-1 --profile default
   
aws events put-targets --rule dyn_snp_multi_volume_lambda_tagging_rule \
  --targets Id=1,arn:aws:lambda:eu-west-2:<account-id>:function:dyn-ec2-allpurposes-tagging,\
   RoleArn=arn:aws:iam::<accountid>:role/Amazon_EventBridge_Invoke_Event_Bus \
  --region eu-west-2 --profile default

aws events put-targets --rule dyn_snp_multi_volume_lambda_tagging_rule \
  --targets Id=1,Arn=arn:aws:events:eu-west-2:<account-id>:event-bus/default,RoleArn=arn:aws:iam::<account-id>:role/Amazon_EventBridge_Invoke_Event_Bus \
  --region eu-west-1 --profile default

aws events put-targets --rule dyn_snp_lambda_tagging_rule \
  --targets Id=1,arn:aws:lambda:eu-west-2:<account-id>:function:dyn-ec2-allpurposes-tagging,RoleArn=arn:aws:iam::<accountid>:role/Amazon_EventBridge_Invoke_Event_Bus \
  --region eu-west-2 --profile default

aws events put-targets --rule dyn_snp_lambda_tagging_rule \
  --targets Id=1,Arn=arn:aws:events:eu-west-2:<account-id>:event-bus/default,RoleArn=arn:aws:iam::<account-id>:role/Amazon_EventBridge_Invoke_Event_Bus \
  --region eu-west-1 --profile default

aws lambda add-permission --function-name dyn-ec2-allpurposes-tagging \
   --statement-id 1 --action lambda:InvokeFunction --principal events.amazonaws.com \
   --source-arn arn:aws:events:eu-west-2:<account-id>:rule/dyn_snp_multi_volume_lambda_tagging_rule --region eu-west-2 --profile default

aws lambda add-permission --function-name dyn-ec2-allpurposes-tagging \
   --statement-id 2 --action lambda:InvokeFunction --principal events.amazonaws.com \
   --source-arn arn:aws:events:eu-west-1:<account-id>:rule/dyn_snp_multi_volume_lambda_tagging_rule --region eu-west-2 --profile default
   
aws lambda add-permission --function-name dyn-ec2-allpurposes-tagging \
   --statement-id 3 --action lambda:InvokeFunction --principal events.amazonaws.com \
   --source-arn arn:aws:events:eu-west-2:<account-id>:rule/dyn_snp_lambda_tagging_rule --region eu-west-2 --profile default 
   
aws lambda add-permission --function-name dyn-ec2-allpurposes-tagging \
   --statement-id 4 --action lambda:InvokeFunction --principal events.amazonaws.com \
   --source-arn arn:aws:events:eu-west-1:<account-id>:rule/dyn_snp_lambda_tagging_rule --region eu-west-2 --profile default
   
