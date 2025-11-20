import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export interface User {
  id: number;
  email: string;
  is_admin: boolean;
  has_voted: boolean;
  created_at?: string;
}

export interface Candidate {
  id: number;
  name: string;
  party: string;
  description: string;
  image_url?: string;
}

export interface VoteResult {
  id: number;
  name: string;
  party: string;
  vote_count: number;
  percentage: number;
}

export interface ApiResponse<T> {
  message?: string;
  error?: string;
  data?: T;
}

// Auth API calls
export const authAPI = {
  register: async (email: string, password: string) => {
    const response = await api.post('/register', { email, password });
    return response.data;
  },

  verifyOTP: async (email: string, otp: string) => {
    const response = await api.post('/verify-otp', { email, otp });
    return response.data;
  },

  login: async (email: string, password: string) => {
    const response = await api.post('/login', { email, password });
    return response.data;
  },

  resendOTP: async (email: string) => {
    const response = await api.post('/resend-otp', { email });
    return response.data;
  },

  getProfile: async () => {
    const response = await api.get('/user/profile');
    return response.data;
  },
};

// Voting API calls
export const votingAPI = {
  getCandidates: async () => {
    const response = await api.get('/candidates');
    return response.data;
  },

  castVote: async (candidateId: number) => {
    const response = await api.post('/vote', { candidate_id: candidateId });
    return response.data;
  },
};

// Admin API calls
export const adminAPI = {
  getResults: async () => {
    const response = await api.get('/admin/results');
    return response.data;
  },

  getAllCandidates: async () => {
    const response = await api.get('/admin/candidates');
    return response.data;
  },

  addCandidate: async (candidateData: {
    name: string;
    party: string;
    description: string;
    image_url: string;
  }) => {
    const response = await api.post('/admin/candidates', candidateData);
    return response.data;
  },
};

export default api;
