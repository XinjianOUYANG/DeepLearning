import numpy as np

def log_marginal_likelihood(Phi, t, alpha, beta):
    """Computes the log of the marginal likelihood."""
    
    Sigma = 1/alpha * Phi @ Phi.T + 1/beta * np.eye(Phi.shape[0])
    
    _, logdet = np.linalg.slogdet(2*np.pi*Sigma)
    
    gauss_exp = np.squeeze(t.T @ np.linalg.inv(Sigma) @ t)
    
    return -0.5 * (logdet + gauss_exp)


def posterior(Phi, t, alpha, beta, return_inverse=False):
    """Computes mean and covariance matrix of the posterior distribution."""
    S_N_inv = alpha * np.eye(Phi.shape[1]) + beta * Phi.T @ Phi
    S_N = np.linalg.inv(S_N_inv)
    m_N = beta * S_N @ Phi.T @ t

    if return_inverse:
        return m_N, S_N, S_N_inv
    else:
        return m_N, S_N

def EM(Phi, t, alpha_0=1e-5, beta_0=1e-5, max_iter=200, rtol=1e-5, verbose=False):
    """
    Jointly infers the posterior sufficient statistics and optimal values 
    for alpha and beta by maximizing the log marginal likelihood.
    
    Args:
        Phi: Design matrix (N x M).
        t: Target value array (N x 1).
        alpha_0: Initial value for alpha.
        beta_0: Initial value for beta.
        max_iter: Maximum number of iterations.
        rtol: Convergence criterion.
        
    Returns:
        alpha, beta, posterior mean, posterior covariance, log-marginal likelihood.
    """
    N, M = Phi.shape

    beta = beta_0
    alpha = alpha_0
    
    mlls = []

    for i in range(max_iter):
        beta_prev = beta
        alpha_prev = alpha

        # E-step (p(W|t,alpha,beta))
        m_N, S_N = posterior(Phi, t, alpha, beta)

        # M-step
        alpha = M/(m_N.T@m_N + np.trace(S_N))
        beta = N/((t-(Phi @ m_N)).T @ (t-(Phi @ m_N)) + np.trace(Phi @ S_N @ Phi.T))
        
        # Compute log-marginal likelihood
        mlls.append(log_marginal_likelihood(Phi, t, alpha=alpha, beta=beta))
        
        if np.isclose(alpha_prev, alpha, rtol=rtol) and np.isclose(beta_prev, beta, rtol=rtol):
            if verbose:
                print(f'Convergence after {i + 1} iterations.')
            return alpha, beta, m_N, S_N, mlls

    if verbose:
        print(f'Stopped after {max_iter} iterations.')
    
    return alpha, beta, m_N, S_N, mlls
    