import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const Home: React.FC = () => {
  const { isAuthenticated, user } = useAuth();

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-lg-8">
          <div className="text-center mb-5">
            <h1 className="display-4 fw-bold text-primary mb-3">🗳️ E-Voting System</h1>
            <p className="lead text-muted">
              Secure, transparent, and accessible digital voting platform
            </p>
          </div>

          {!isAuthenticated ? (
            <div className="row g-4">
              <div className="col-md-6">
                <div className="card h-100 shadow-sm">
                  <div className="card-body text-center">
                    <h5 className="card-title">New Voter?</h5>
                    <p className="card-text">
                      Create your account and get verified to participate in voting.
                    </p>
                    <Link to="/register" className="btn btn-primary">
                      Register Now
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col-md-6">
                <div className="card h-100 shadow-sm">
                  <div className="card-body text-center">
                    <h5 className="card-title">Already Registered?</h5>
                    <p className="card-text">Sign in to your account and cast your vote.</p>
                    <Link to="/login" className="btn btn-outline-primary">
                      Login
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div className="text-center">
              <div className="alert alert-success" role="alert">
                <h4 className="alert-heading">Welcome, {user?.email}!</h4>
                <p>You are successfully logged in to the E-Voting System.</p>
                <hr />
                <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                  {!user?.has_voted ? (
                    <Link to="/vote" className="btn btn-success btn-lg">
                      Cast Your Vote
                    </Link>
                  ) : (
                    <div>
                      <p className="mb-2">✅ You have already voted!</p>
                      {user?.is_admin && (
                        <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                          <Link to="/admin" className="btn btn-info">
                            📊 View Results
                          </Link>
                          <Link to="/manage-candidates" className="btn btn-warning">
                            🏛️ Manage Candidates
                          </Link>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </div>

              {/* Admin Quick Actions */}
              {user?.is_admin && (
                <div className="row g-3 mt-4">
                  <div className="col-12">
                    <h5 className="text-muted">👑 Admin Quick Actions</h5>
                  </div>
                  <div className="col-md-4">
                    <div className="card bg-light">
                      <div className="card-body text-center">
                        <h6 className="card-title">📊 Results Dashboard</h6>
                        <p className="card-text small">View voting results and statistics</p>
                        <Link to="/admin" className="btn btn-info btn-sm">
                          Open Dashboard
                        </Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="card bg-light">
                      <div className="card-body text-center">
                        <h6 className="card-title">🏛️ Manage Candidates</h6>
                        <p className="card-text small">Add, edit, or remove candidates</p>
                        <Link to="/manage-candidates" className="btn btn-warning btn-sm">
                          Manage
                        </Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="card bg-light">
                      <div className="card-body text-center">
                        <h6 className="card-title">🗳️ Voting Page</h6>
                        <p className="card-text small">Preview the voting experience</p>
                        <Link to="/vote" className="btn btn-success btn-sm">
                          Preview
                        </Link>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}

          <div className="mt-5">
            <h3 className="text-center mb-4">How It Works</h3>
            <div className="row g-4">
              <div className="col-md-3">
                <div className="text-center">
                  <div
                    className="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center"
                    style={{ width: '60px', height: '60px' }}
                  >
                    <span className="fs-4">1</span>
                  </div>
                  <h6 className="mt-3">Register</h6>
                  <small className="text-muted">Create account with email</small>
                </div>
              </div>
              <div className="col-md-3">
                <div className="text-center">
                  <div
                    className="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center"
                    style={{ width: '60px', height: '60px' }}
                  >
                    <span className="fs-4">2</span>
                  </div>
                  <h6 className="mt-3">Verify</h6>
                  <small className="text-muted">Confirm with OTP</small>
                </div>
              </div>
              <div className="col-md-3">
                <div className="text-center">
                  <div
                    className="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center"
                    style={{ width: '60px', height: '60px' }}
                  >
                    <span className="fs-4">3</span>
                  </div>
                  <h6 className="mt-3">Vote</h6>
                  <small className="text-muted">Choose your candidate</small>
                </div>
              </div>
              <div className="col-md-3">
                <div className="text-center">
                  <div
                    className="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center"
                    style={{ width: '60px', height: '60px' }}
                  >
                    <span className="fs-4">4</span>
                  </div>
                  <h6 className="mt-3">Results</h6>
                  <small className="text-muted">View vote counts</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
