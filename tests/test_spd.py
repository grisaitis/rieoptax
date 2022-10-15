
from absl.testing import absltest
from chex import assert_trees_all_close
from rieoptax.geometry.spd import SPDAffineInvariant
class TestSPDAffineInvarinat(absltest.TestCase):
    
    manifold = SPDAffineInvariant(2,2)
    def test_exp():
        manifold = SPDAffineInvariant()
        tv =jnp.array([[2.0, 0.0], [0.0, 2.0]])
        bp =jnp.array([[1.0, 0.0], [0.0, 1.0]])
        expected=jnp.array([[jnp.exp(2), 0.0], [0.0, jnp.exp(2)]])
        assert_trees_all_close(manifold.exp(bp, tv), expected)

    def test_log():
        
    def test_pt():
        
    def test_inp():
        
    def test_
    