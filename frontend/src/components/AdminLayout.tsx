import React from 'react';
import { Link } from 'react-router-dom';

const AdminLayout: React.FC<{ children: React.ReactNode; title: string; currentPage: string }> = ({
  children,
  title,
  currentPage,
}) => {
  const navItems = [
    { path: '/admin', label: '📊 Results Dashboard', key: 'admin' },
    { path: '/manage-candidates', label: '🏛️ Manage Candidates', key: 'manage-candidates' },
    { path: '/vote', label: '🗳️ Voting Preview', key: 'vote' },
  ];

  return (
    <div className="container mt-4">
      {/* Admin Navigation */}
      <div className="row mb-4">
        <div className="col-12">
          <div className="card bg-primary text-white">
            <div className="card-body">
              <h4 className="card-title mb-3">👑 Admin Panel</h4>
              <nav className="nav nav-pills flex-column flex-sm-row">
                {navItems.map((item) => (
                  <Link
                    key={item.key}
                    to={item.path}
                    className={`nav-link ${
                      currentPage === item.key ? 'active bg-white text-primary' : 'text-white-50'
                    } me-2 mb-1`}
                  >
                    {item.label}
                  </Link>
                ))}
              </nav>
            </div>
          </div>
        </div>
      </div>

      {/* Page Title */}
      <div className="row mb-4">
        <div className="col-12">
          <h2>{title}</h2>
        </div>
      </div>

      {/* Page Content */}
      {children}
    </div>
  );
};

export default AdminLayout;
