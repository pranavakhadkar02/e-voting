import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { votingAPI, Candidate } from '../services/api';
import { toast } from 'react-toastify';

const Vote: React.FC = () => {
  const [candidates, setCandidates] = useState<Candidate[]>([]);
  const [loading, setLoading] = useState(true);
  const [voting, setVoting] = useState(false);

  const { user, updateUser } = useAuth();

  useEffect(() => {
    fetchCandidates();
  }, []);

  const fetchCandidates = async () => {
    try {
      const response = await votingAPI.getCandidates();
      setCandidates(response.candidates);
    } catch (error: any) {
      toast.error('Failed to load candidates');
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (candidateId: number) => {
    if (user?.has_voted) {
      toast.error('You have already voted');
      return;
    }

    const confirmed = window.confirm(
      'Are you sure you want to vote for this candidate? This action cannot be undone.'
    );

    if (!confirmed) return;

    setVoting(true);
    try {
      await votingAPI.castVote(candidateId);
      toast.success('Vote cast successfully!');
      // Update user state to reflect that they have voted
      updateUser({ has_voted: true });
    } catch (error: any) {
      toast.error(error.response?.data?.error || 'Failed to cast vote');
    } finally {
      setVoting(false);
    }
  };

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  if (user?.has_voted) {
    return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-lg-8">
            <div className="alert alert-success text-center">
              <h4 className="alert-heading">✅ Vote Submitted Successfully!</h4>
              <p>
                Thank you for participating in the election. Your vote has been recorded securely.
              </p>
              <hr />
              <p className="mb-0">Results will be available after the voting period ends.</p>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-lg-10">
          <h2 className="text-center mb-5">Cast Your Vote</h2>

          <div className="alert alert-warning" role="alert">
            <strong>Important:</strong> You can only vote once. Please choose carefully as this
            action cannot be undone.
          </div>

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
                    />
                  )}
                  <div className="card-body d-flex flex-column">
                    <h5 className="card-title">{candidate.name}</h5>
                    <h6 className="card-subtitle mb-2 text-muted">{candidate.party}</h6>
                    <p className="card-text flex-grow-1">{candidate.description}</p>
                    <button
                      className="btn btn-primary mt-auto"
                      onClick={() => handleVote(candidate.id)}
                      disabled={voting}
                    >
                      {voting ? (
                        <>
                          <span className="spinner-border spinner-border-sm me-2" />
                          Voting...
                        </>
                      ) : (
                        'Vote for ' + candidate.name
                      )}
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {candidates.length === 0 && (
            <div className="text-center">
              <div className="alert alert-info">
                No candidates available for voting at this time.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Vote;
