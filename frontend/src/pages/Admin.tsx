import React, { useState, useEffect } from 'react';
import { adminAPI, VoteResult } from '../services/api';
import { toast } from 'react-toastify';
import AdminLayout from '../components/AdminLayout';

interface AdminStats {
  results: VoteResult[];
  total_votes: number;
  total_users: number;
}

const Admin: React.FC = () => {
  const [stats, setStats] = useState<AdminStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async () => {
    try {
      const response = await adminAPI.getResults();
      setStats(response);
    } catch (error: any) {
      toast.error('Failed to load results');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <AdminLayout title="📊 Results Dashboard" currentPage="admin">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </AdminLayout>
    );
  }

  if (!stats) {
    return (
      <AdminLayout title="📊 Results Dashboard" currentPage="admin">
        <div className="alert alert-danger">Failed to load voting results.</div>
      </AdminLayout>
    );
  }

  const winner = stats.results.length > 0 ? stats.results[0] : null;

  return (
    <AdminLayout title="📊 Results Dashboard" currentPage="admin">
      <div className="row">
        <div className="col-12">
          {/* Statistics Cards */}
          <div className="row g-4 mb-5">
            <div className="col-md-4">
              <div className="card bg-primary text-white text-center">
                <div className="card-body">
                  <h3 className="card-title">{stats.total_votes}</h3>
                  <p className="card-text">Total Votes Cast</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card bg-success text-white text-center">
                <div className="card-body">
                  <h3 className="card-title">{stats.total_users}</h3>
                  <p className="card-text">Registered Users</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card bg-info text-white text-center">
                <div className="card-body">
                  <h3 className="card-title">
                    {stats.total_users > 0
                      ? ((stats.total_votes / stats.total_users) * 100).toFixed(1) + '%'
                      : '0%'}
                  </h3>
                  <p className="card-text">Turnout Rate</p>
                </div>
              </div>
            </div>
          </div>

          {/* Winner Announcement */}
          {winner && stats.total_votes > 0 && (
            <div className="alert alert-success text-center mb-5">
              <h4 className="alert-heading">🎉 Current Leader</h4>
              <h3 className="mb-2">{winner.name}</h3>
              <p className="mb-1">
                <strong>{winner.party}</strong>
              </p>
              <p className="mb-0">
                {winner.vote_count} votes ({winner.percentage}%)
              </p>
            </div>
          )}

          {/* Results Table */}
          <div className="card">
            <div className="card-header">
              <h5 className="mb-0">Detailed Results</h5>
            </div>
            <div className="card-body">
              {stats.results.length === 0 ? (
                <div className="text-center text-muted">
                  <p>No votes have been cast yet.</p>
                </div>
              ) : (
                <div className="table-responsive">
                  <table className="table table-hover">
                    <thead className="table-dark">
                      <tr>
                        <th>Rank</th>
                        <th>Candidate</th>
                        <th>Party</th>
                        <th>Votes</th>
                        <th>Percentage</th>
                        <th>Progress</th>
                      </tr>
                    </thead>
                    <tbody>
                      {stats.results.map((result, index) => (
                        <tr key={result.id} className={index === 0 ? 'table-success' : ''}>
                          <td>
                            <span
                              className={`badge ${index === 0 ? 'bg-warning' : 'bg-secondary'}`}
                            >
                              #{index + 1}
                            </span>
                          </td>
                          <td>
                            <strong>{result.name}</strong>
                            {index === 0 && <span className="ms-2">👑</span>}
                          </td>
                          <td>{result.party}</td>
                          <td>
                            <strong>{result.vote_count}</strong>
                          </td>
                          <td>{result.percentage}%</td>
                          <td style={{ width: '200px' }}>
                            <div className="progress">
                              <div
                                className={`progress-bar ${
                                  index === 0
                                    ? 'bg-success'
                                    : index === 1
                                    ? 'bg-info'
                                    : 'bg-secondary'
                                }`}
                                role="progressbar"
                                style={{ width: `${result.percentage}%` }}
                                aria-valuenow={result.percentage}
                                aria-valuemin={0}
                                aria-valuemax={100}
                              >
                                {result.percentage > 10 && `${result.percentage}%`}
                              </div>
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>

          {/* Refresh Button */}
          <div className="text-center mt-4">
            <button className="btn btn-outline-primary" onClick={fetchResults} disabled={loading}>
              {loading ? (
                <>
                  <span className="spinner-border spinner-border-sm me-2" />
                  Refreshing...
                </>
              ) : (
                <>🔄 Refresh Results</>
              )}
            </button>
          </div>

          {/* Footer Note */}
          <div className="mt-5">
            <div className="alert alert-light">
              <small className="text-muted">
                <strong>Note:</strong> Results are updated in real-time. This dashboard is only
                accessible to admin users.
              </small>
            </div>
          </div>
        </div>
      </div>
    </AdminLayout>
  );
};

export default Admin;
