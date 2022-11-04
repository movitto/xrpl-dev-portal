from xrpl.clients import JsonRpcClient
from xrpl.models import IssuedCurrencyAmount, TrustSet
from xrpl.transaction import (safe_sign_and_autofill_transaction,
                              send_reliable_submission)
from xrpl.models import TrustSetFlag
from xrpl.utils import str_to_hex
from xrpl.wallet import generate_faucet_wallet

client = JsonRpcClient("https://s.altnet.rippletest.net:51234") # connect to testnet

token_name = "USD"

# Amount a trustline can handle
value = "0"

# Address to unfreeze trustline
target_addr = generate_faucet_wallet(client=client).classic_address

# Sender wallet
sender_wallet = generate_faucet_wallet(client=client)

# Build trustline freeze transaction
trustset = TrustSet(account=sender_wallet.classic_address, limit_amount=IssuedCurrencyAmount(
    currency=token_name,
    issuer=target_addr,
    value = value 
),
flags=TrustSetFlag.TF_CLEAR_FREEZE)

# Sign and Submit transaction
stxn = safe_sign_and_autofill_transaction(trustset, sender_wallet, client)
stxn_response = send_reliable_submission(stxn, client)

# Parse response for result
stxn_result = stxn_response.result

# Print result and transaction hash
if stxn_result["meta"]["TransactionResult"] == "tesSUCCESS":
  print(f'Successfully enabled no freeze for {sender_wallet.classic_address}')
  print(stxn_result["hash"])
else:
  print(stxn_result["meta"]["TransactionResult"])
  print(stxn_result["hash"])
