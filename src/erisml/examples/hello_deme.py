"""
Hello DEME - A minimal example of the ErisML Ethics Engine.
This script verifies that the library is installed and functioning.
"""
import sys

# Import the core engine components
try:
    from erisml.ethics import MoralTensor, EthicalFacts
except ImportError:
    # Fallback for local testing if package isn't installed yet
    sys.path.append(".") 
    from src.erisml.ethics import MoralTensor, EthicalFacts

def main():
    print("\n🍎 ErisML System Initialization...")
    print("--------------------------------")
    
    try:
        # 1. Verify we can create a MoralTensor (The math core)
        # Creating a simple 1x1x1 tensor (1 party, 1 timestep, 1 action)
        tensor = MoralTensor.from_dense([[[0.8]]], axis_names=("n", "tau", "a"))
        print(f"✅ Moral Tensor System: ONLINE")
        print(f"   - Tensor Rank: {tensor.rank}")
        print(f"   - Shape: {tensor.shape}")

        # 2. Verify we can define Ethical Facts (The data structure)
        facts = EthicalFacts(
            harm_risk=0.1,
            benefit_potential=0.9,
            rights_at_stake=["none"],
            consent_status="explicit_consent"
        )
        print(f"✅ Ethical Facts System: ONLINE")
        print(f"   - Consent Status: {facts.consent_status}")
        
        # 3. Success Message
        print("\n🎉 SUCCESS: ErisML is correctly installed and running.")
        
    except ImportError as e:
        print(f"❌ CRITICAL ERROR: Could not import core modules. {e}")
    except Exception as e:
        print(f"❌ RUNTIME ERROR: {e}")

if __name__ == "__main__":
    main()
