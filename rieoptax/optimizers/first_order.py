from rieoptax.core import RiemannianGradientTransformation

from rieoptax.optimizers.combine import chain
from rieoptax.optimizers.privacy import differentially_private_aggregate
from rieoptax.optimizers.transforms import scale_by_learning_rate


def rsgd(learning_rate: float) -> RiemannianGradientTransformation:
    """Riemannian stochastic gradient descent."""
    return scale_by_learning_rate(learning_rate)

def radam(learning_rate: float) -> RiemannianGradientTransformation:
    """Riemannian adaptive moment estimation (ADAM)."""
    return 



def dp_rsgd(
    learning_rate: float, norm_clip: float, sigma: float, seed: int
) -> RiemannianGradientTransformation:
    "Differenitally private riemannian (stochastic) gradient descent."
    return chain(
        differentially_private_aggregate(norm_clip=norm_clip, sigma=sigma, seed=seed),
        scale_by_learning_rate(learning_rate),
    )
