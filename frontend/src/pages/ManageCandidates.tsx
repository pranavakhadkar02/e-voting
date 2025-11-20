import React, { useState, useEffect } from 'react';
import { adminAPI, Candidate } from '../services/api';
import { toast } from 'react-toastify';
import AdminLayout from '../components/AdminLayout';

interface CandidateWithVotes extends Candidate {
  vote_count: number;
}

const ManageCandidates: React.FC = () => {
  const [candidates, setCandidates] = useState<CandidateWithVotes[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddForm, setShowAddForm] = useState(false);
  const [editingCandidate, setEditingCandidate] = useState<CandidateWithVotes | null>(null);
  const [formData, setFormData] = useState({
    name: '',
    party: '',
    description: '',
    image_url: '',
  });
  const [submitting, setSubmitting] = useState(false);
  const [deleting, setDeleting] = useState<number | null>(null);

  useEffect(() => {
    fetchCandidates();
  }, []);

  const fetchCandidates = async () => {
    try {
      const response = await adminAPI.getAllCandidates();
      setCandidates(response.candidates);
    } catch (error: any) {
      toast.error('Failed to load candidates');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.name.trim() || !formData.party.trim()) {
      toast.error('Name and party are required');
      return;
    }

    setSubmitting(true);
    try {
      if (editingCandidate) {
        await adminAPI.updateCandidate(editingCandidate.id, formData);
        toast.success('Candidate updated successfully!');
      } else {
        await adminAPI.addCandidate(formData);
        toast.success('Candidate added successfully!');
      }
      resetForm();
      fetchCandidates();
    } catch (error: any) {
      toast.error(
        error.response?.data?.error || `Failed to ${editingCandidate ? 'update' : 'add'} candidate`
      );
    } finally {
      setSubmitting(false);
    }
  };

  const resetForm = () => {
    setFormData({ name: '', party: '', description: '', image_url: '' });
    setShowAddForm(false);
    setEditingCandidate(null);
  };

  const handleEdit = (candidate: CandidateWithVotes) => {
    setFormData({
      name: candidate.name,
      party: candidate.party,
      description: candidate.description,
      image_url: candidate.image_url || '',
    });
    setEditingCandidate(candidate);
    setShowAddForm(true);
  };

  const handleDelete = async (candidate: CandidateWithVotes) => {
    if (
      !window.confirm(
        `Are you sure you want to delete ${candidate.name}?\n\nThis action cannot be undone.`
      )
    ) {
      return;
    }

    setDeleting(candidate.id);
    try {
      await adminAPI.deleteCandidate(candidate.id);
      toast.success('Candidate deleted successfully!');
      fetchCandidates();
    } catch (error: any) {
      toast.error(error.response?.data?.error || 'Failed to delete candidate');
    } finally {
      setDeleting(null);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  if (loading) {
    return (
      <AdminLayout title="🏛️ Manage Candidates" currentPage="manage-candidates">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </AdminLayout>
    );
  }

  return (
    <AdminLayout title="🏛️ Manage Candidates" currentPage="manage-candidates">
      <div className="row">
        <div className="col-12">
          <div className="d-flex justify-content-between align-items-center mb-4">
            <h5 className="text-muted mb-0">Candidate Management System</h5>
            <button
              className="btn btn-primary"
              onClick={() => {
                if (showAddForm) {
                  resetForm();
                } else {
                  setShowAddForm(true);
                }
              }}
            >
              {showAddForm ? '✕ Cancel' : '+ Add New Candidate'}
            </button>
          </div>

          {/* Add/Edit Candidate Form */}
          {showAddForm && (
            <div className="card mb-4">
              <div className="card-header">
                <h5 className="mb-0">
                  {editingCandidate ? `Edit ${editingCandidate.name}` : 'Add New Candidate'}
                </h5>
              </div>
              <div className="card-body">
                <form onSubmit={handleSubmit}>
                  <div className="row g-3">
                    <div className="col-md-6">
                      <label htmlFor="name" className="form-label">
                        Candidate Name <span className="text-danger">*</span>
                      </label>
                      <input
                        type="text"
                        className="form-control"
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleInputChange}
                        required
                      />
                    </div>
                    <div className="col-md-6">
                      <label htmlFor="party" className="form-label">
                        Party Name <span className="text-danger">*</span>
                      </label>
                      <input
                        type="text"
                        className="form-control"
                        id="party"
                        name="party"
                        value={formData.party}
                        onChange={handleInputChange}
                        required
                      />
                    </div>
                    <div className="col-12">
                      <label htmlFor="description" className="form-label">
                        Description
                      </label>
                      <textarea
                        className="form-control"
                        id="description"
                        name="description"
                        rows={3}
                        value={formData.description}
                        onChange={handleInputChange}
                        placeholder="Brief description of the candidate's platform or background"
                      />
                    </div>
                    <div className="col-12">
                      <label htmlFor="image_url" className="form-label">
                        Image URL
                      </label>
                      <input
                        type="url"
                        className="form-control"
                        id="image_url"
                        name="image_url"
                        value={formData.image_url}
                        onChange={handleInputChange}
                        placeholder="https://example.com/candidate-photo.jpg"
                      />
                      <div className="form-text">Leave empty to use default placeholder image</div>
                    </div>
                  </div>
                  <div className="mt-3">
                    <button type="submit" className="btn btn-success me-2" disabled={submitting}>
                      {submitting ? (
                        <>
                          <span className="spinner-border spinner-border-sm me-2" />
                          {editingCandidate ? 'Updating...' : 'Adding...'}
                        </>
                      ) : editingCandidate ? (
                        'Update Candidate'
                      ) : (
                        'Add Candidate'
                      )}
                    </button>
                    <button type="button" className="btn btn-secondary" onClick={resetForm}>
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          )}

          {/* Candidates List */}
          <div className="card">
            <div className="card-header">
              <h5 className="mb-0">Current Candidates ({candidates.length})</h5>
            </div>
            <div className="card-body">
              {candidates.length === 0 ? (
                <div className="text-center text-muted py-4">
                  <h6>No candidates found</h6>
                  <p>Click "Add New Candidate" to get started</p>
                </div>
              ) : (
                <div className="row g-4">
                  {candidates.map((candidate) => (
                    <div key={candidate.id} className="col-md-6 col-lg-4">
                      <div className="card h-100 shadow-sm">
                        {candidate.image_url && (
                          <img
                            src={candidate.image_url}
                            className="card-img-top"
                            alt={candidate.name}
                            style={{ height: '200px', objectFit: 'cover' }}
                            onError={(e) => {
                              const target = e.target as HTMLImageElement;
                              target.src = 'https://via.placeholder.com/150x200?text=No+Image';
                            }}
                          />
                        )}
                        <div className="card-body d-flex flex-column">
                          <h5 className="card-title">{candidate.name}</h5>
                          <h6 className="card-subtitle mb-2 text-muted">{candidate.party}</h6>
                          <p className="card-text flex-grow-1">
                            {candidate.description || 'No description provided'}
                          </p>

                          <div className="mt-auto">
                            <div className="d-flex justify-content-between align-items-center mb-2">
                              <small className="text-muted">Vote Count:</small>
                              <span className="badge bg-primary fs-6">
                                {candidate.vote_count} votes
                              </span>
                            </div>

                            <div className="btn-group w-100" role="group">
                              <button
                                type="button"
                                className="btn btn-outline-primary btn-sm"
                                onClick={() => handleEdit(candidate)}
                                disabled={deleting === candidate.id}
                              >
                                ✏️ Edit
                              </button>
                              <button
                                type="button"
                                className="btn btn-outline-danger btn-sm"
                                onClick={() => handleDelete(candidate)}
                                disabled={deleting === candidate.id}
                              >
                                {deleting === candidate.id ? (
                                  <>
                                    <span
                                      className="spinner-border spinner-border-sm me-1"
                                      style={{ width: '12px', height: '12px' }}
                                    />
                                    Deleting...
                                  </>
                                ) : (
                                  '🗑️ Delete'
                                )}
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Refresh Button */}
          <div className="text-center mt-4">
            <button
              className="btn btn-outline-primary"
              onClick={fetchCandidates}
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="spinner-border spinner-border-sm me-2" />
                  Refreshing...
                </>
              ) : (
                <>🔄 Refresh Candidates</>
              )}
            </button>
          </div>

          {/* Help Section */}
          <div className="alert alert-info mt-4">
            <h6 className="alert-heading">💡 Tips for Managing Candidates</h6>
            <ul className="mb-0">
              <li>
                <strong>Name & Party:</strong> Required fields for all candidates
              </li>
              <li>
                <strong>Description:</strong> Help voters understand each candidate's platform
              </li>
              <li>
                <strong>Images:</strong> Use high-quality photos (recommended: 300x400px)
              </li>
              <li>
                <strong>Editing:</strong> Click "Edit" to prefill the form with existing data
              </li>
              <li>
                <strong>Vote Counts:</strong> Updated in real-time as votes are cast
              </li>
            </ul>
          </div>
        </div>
      </div>
    </AdminLayout>
  );
};

export default ManageCandidates;
